import { ApiError } from "../utils/apiError.js";
import { ApiResponce } from "../utils/apiResponce.js";
import { asyncHandler } from "../utils/asyncHandler.js";
import { Seller } from "../models/sellers/seller.models.js";

export const sellerRegister = asyncHandler(async (req, res) => {
  // data --> validate { entry, exits } --> create --> chack --> return
  const { username, fullName, email, password } = req.body;
  if (
    [username, fullName, email, password].some((field) => field?.trim() === "")
  ) {
    throw new ApiError(400, "All field is nessesary");
  }
  if (await Seller.findOne({ username })) {
    throw new ApiError(400, "User already exits");
  }
  const newSeller = await Seller.create({
    username,
    fullName,
    email,
    password,
  });

  const newCreatedSeller = await Seller.findById(newSeller._id).select(
    "-password -_id -__v"
  );

  if (!newCreatedSeller) {
    throw new ApiError(500, "unfortunately, seller not created");
  }
  return res
    .status(201)
    .json(
      new ApiResponce(200, newCreatedSeller, "seller created successfully")
    );
});

export const sellerLogin = asyncHandler(async (req, res) => {
  // data --> chack (empty, username exits) -->
  const { username, password, saveInfo } = req.body;

  if (
    [username, password, saveInfo].some(
      (field) => field?.toString().trim() === ""
    )
  ) {
    throw new ApiError(400, "All field is requide");
  }
  const SearchSeller = await Seller.findOne({ username });

  if (!SearchSeller) {
    throw new ApiError(409, "Seller not exits");
  }

  if (!(await SearchSeller.isPasswordCorrect(password))) {
    throw new ApiError(400, "Incorrect password");
  }

  if (saveInfo) {
    const { refreshToken, accessToken } =
      await accessAndRefreshTokenGenrator(SearchSeller);

    const sellerDetails = await Seller.findByIdAndUpdate(
      SearchSeller._id,
      {
        $set: {
          lastLogin: Date.now(),
          refreshToken: refreshToken,
        },
      },
      { new: true }
    ).select("-password -refreshToken");

    const options = {
      httpOnly: true,
      secure: true,
    };

    console.log(`status: 200 - login successfully `);

    return res
      .status(200)
      .cookie("accessToken", accessToken, options)
      .cookie("refreshToken", refreshToken, options)
      .json(new ApiResponce(200, sellerDetails, "login successfully"));
  } else {
    const accessToken = await SearchSeller.genrateAccessToken();

    const sellerDetails = await User.findByIdAndUpdate(
      SearchSeller._id,
      {
        $set: {
          lastLogin: Date.now(),
          refreshToken: null,
        },
      },
      { new: true }
    ).select("-password -refreshToken");

    const options = {
      httpOnly: true,
      secure: true,
    };

    console.log(`status: 200 - login successfully `);

    return res
      .status(200)
      .cookie("accessToken", accessToken, options)
      .json(new ApiResponce(200, sellerDetails, "login successfully"));
  }
});

export const logOutUser = asyncHandler(async (req, res) => {
  // chack user login or not by auth midileware
  // take user id by middleware and make refresh token in database
  // remove all cookies
  // console.log(req.userId)
  if (!req.userId) {
    throw new ApiError(500, "auth middle not work properlly");
  }
  try {
    await User.findByIdAndUpdate(req.userId, {
      $set: {
        refreshToken: null,
      },
    }).select("-password ");
  } catch (error) {
    throw ApiError(500, error?.massage || "server not connected with database");
  }

  const options = {
    httpOnly: true,
    secure: true,
  };

  return res
    .status(200)
    .clearCookie("accessToken", options)
    .clearCookie("refreshToken", options)
    .json(new ApiResponce(200, {}, "User logged Out Successfully"));
});

export const setAvtar = asyncHandler(async (req, res) => {
  // retrebe data by req.userId
  // retrebe file server path by multer meddleware
  // upload the file in cloudinary and save url on user

  if (!req.file) {
    throw ApiError(400, "file not recived");
  }

  const localAvatarPath = req.file?.path;

  if (!localAvatarPath) {
    throw new ApiError(404, "File path not found");
  }

  const responce = await uploadFileToCloudinary(localAvatarPath);

  if (!responce) {
    throw new ApiError(500, "unfortunataly, file uploadation failds!!");
  }

  try {
    await Seller.findByIdAndUpdate(
      req.userId,
      {
        $set: {
          avatar: responce.url,
        },
      },
      { new: true }
    );
  } catch (error) {
    throw new ApiError(500, error?.massage || "Avatar set faild");
  }
  const userAvatar = await Seller.findById(req.userId).select(
    "-password -refreshToken"
  );
  return res.status(200).json(new ApiResponce(200, { userAvatar }, ""));
});
