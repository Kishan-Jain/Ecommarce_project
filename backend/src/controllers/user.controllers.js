import { asyncHandler } from "../utils/asyncHandler.js";
import { ApiError } from "../utils/apiError.js";
import { ApiResponce } from "../utils/apiResponce.js";
import { User } from "../models/users/user.models.js";
import { accessAndRefreshTokenGenrator } from "../utils/accessRefreshTokenGenrator.js";
import { uploadFileToCloudinary } from "../utils/cloudinary.js";

export const userRegister = asyncHandler(async (req, res) => {
  // register user :
  // 1. data --> validate (data / already exits) ---> server store --> db - model - data set

  const { username, fullName, email, password } = req.body;
  if (
    [username, fullName, email, password].some((field) => field?.trim() === "")
  ) {
    throw new ApiError(400, "All fields are required");
  }
  if (await User.findOne({ username })) {
    throw new ApiError(409, "Username allready exits");
  }

  const newUser = await User.create({
    username,
    fullName,
    email,
    password,
  });

  const newCreaterUser = await User.findById(newUser._id).select(
    "-password -refreshToken -__v"
  );

  if (!newCreaterUser) {
    throw new ApiError(500, "unfortunately, user not created");
  }
  console.log("statusCode: 201 - user registed successfully");
  return res
    .status(201)
    .json(new ApiResponce(200, newCreaterUser, "user registered successfully"));
});

export const userLogin = asyncHandler(async (req, res) => {
  // data from frount {username, password } --> chack is empty --> username exit or not -->
  // varify password -- > access token + login permission
  if (!req.body){
    throw ApiError(400, "No any data recived")
  }
  const { username, password, saveInfo } = req.body;

  if ([username, password, saveInfo].some((field) => (field?.toString()).trim() === "")) {
    throw new ApiError(400, "All field is requide");
  }
  const SearchUser = await User.findOne({ username });

  if (!SearchUser) {
    throw new ApiError(409, "User not exits");
  }

  if (!(await SearchUser.isPasswordCorrect(password))) {
    throw new ApiError(400, "Incorrect password");
  }

  if (saveInfo){
  const { refreshToken, accessToken } =
    await accessAndRefreshTokenGenrator(SearchUser);

  const userDetails = await User.findByIdAndUpdate(
    SearchUser._id,
    {
      $set: {
        lastLogin: Date.now(),
        refreshToken: refreshToken,
      },
    },
    { new: true }
  ).select("-password");

  const options = {
    httpOnly: true,
    secure: true,
  };

  console.log(`status: 200 - login successfully `);

  return res
    .status(200)
    .cookie("accessToken", accessToken, options)
    .cookie("refreshToken", refreshToken, options)
    .json(new ApiResponce(200, userDetails, "login successfully"));
} else {

  const accessToken = await SearchUser.genrateAccessToken()

const userDetails = await User.findByIdAndUpdate(
  SearchUser._id,
  {
    $set: {
      lastLogin: Date.now(),
      refreshToken: undefined,
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
  .json(new ApiResponce(200, userDetails, "login successfully"));

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
  console.log(req.file);
  const localAvatarPath = req.file?.path;

  if (!localAvatarPath) {
    throw new ApiError(404, "File not exits");
  }

  const responce = await uploadFileToCloudinary(localAvatarPath);

  if (!responce) {
    throw new ApiError(500, "unfortunataly, file not upload successfully!!");
  }

  console.log(responce);
  try {
    await User.findByIdAndUpdate(
      req.userId,
      {
        $set: {
          avatar: responce.url,
        },
      },
      { new: true }
    );
  } catch (error) {
    throw new ApiError(500, error?.massage || "server db connection error");
  }
  const userAvatar = await User.findById(req.userId).select(
    "-password -refreshToken"
  );
  return res.status(200).json(new ApiResponce(200, { userAvatar }, ""));
});

export const addAddress = asyncHandler(async (req, res) => {
    // add address 
    
    const {area, city, state, pincode} = req.body

    if (
      [area, city, state, pincode].some((field) => (field?.toString()).trim() === "")
    ){
      throw new ApiError(400, "All fields are required")
    }
    
    try { 
      const userAddress =  await User.findById(req.userId).select("address")

      userAddress.address.push({area, city, state, pincode})
      userAddress.save({validateBeforeSave : false, new : true})

    } catch (error) {
      throw new ApiError( 500, error || "Address not set")
    }

    const SearchUser = await User.findById(req.userId).select("-password -refreshToken")
    return res
    .status(200)
    .json(
        new ApiResponce(200, SearchUser, "massage : done")
    )

})