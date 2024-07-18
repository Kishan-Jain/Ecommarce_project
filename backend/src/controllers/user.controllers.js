import { asyncHandler } from "../utils/asyncHandler.js";
import { ApiError } from "../utils/apiError.js";
import { ApiResponse } from "../utils/apiResponse.js";
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
    .json(new ApiResponse(200, newCreaterUser, "user registered successfully"));
});

export const userLogin = asyncHandler(async (req, res) => {
  // data from frount {username, password } --> chack is empty --> username exit or not -->
  // varify password -- > access token + login permission
  if (!req.body) {
    throw ApiError(400, "No any data recived");
  }
  const { username, password, saveInfo } = req.body;

  if (
    [username, password, saveInfo].some(
      (field) => field?.toString().trim() === ""
    )
  ) {
    throw new ApiError(400, "All field is requide");
  }
  const SearchUser = await User.findOne({ username });

  if (!SearchUser) {
    throw new ApiError(409, "User not exits");
  }

  if (!(await SearchUser.isPasswordCorrect(password))) {
    throw new ApiError(400, "Incorrect password");
  }

  if (saveInfo) {
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
      .json(new ApiResponse(200, userDetails, "login successfully"));
  } else {
    const accessToken = await SearchUser.genrateAccessToken();

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
      .json(new ApiResponse(200, userDetails, "login successfully"));
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
    .json(new ApiResponse(200, {}, "User logged Out Successfully"));
});

export const setAvtar = asyncHandler(async (req, res) => {
  // retrebe data by req.userId
  // retrebe file server path by multer meddleware
  // upload the file in cloudinary and save url on user
  // Check if user is authenticated
  if (!req.userId) {
    throw new ApiError(400, "User not Authenticate");
  }
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
  return res.status(200).json(new ApiResponse(200, { userAvatar }, ""));
});

export const addAddress = asyncHandler(async (req, res) => {
  // add address

  const { area, city, state, pincode } = req.body;

  if (
    [area, city, state, pincode].some(
      (field) => field?.toString().trim() === ""
    )
  ) {
    throw new ApiError(400, "All fields are required");
  }

  try {
    const userAddress = await User.findById(req.userId).select("address");

    userAddress.address.push({ area, city, state, pincode });
    userAddress.save({ validateBeforeSave: false, new: true });
  } catch (error) {
    throw new ApiError(500, error || "Address not set");
  }

  const SearchUser = await User.findById(req.userId).select(
    "-password -refreshToken"
  );
  return res
    .status(200)
    .json(new ApiResponse(200, SearchUser, "massage : done"));
});

export const addProductOnCart = asyncHandler(async (req, res) => {
  // add address

  const { area, city, state, pincode } = req.body;

  if (
    [area, city, state, pincode].some(
      (field) => field?.toString().trim() === ""
    )
  ) {
    throw new ApiError(400, "All fields are required");
  }

  try {
    const userAddress = await User.findById(req.userId).select("address");

    userAddress.address.push({ area, city, state, pincode });
    userAddress.save({ validateBeforeSave: false, new: true });
  } catch (error) {
    throw new ApiError(500, error || "Address not set");
  }

  const SearchUser = await User.findById(req.userId).select(
    "-password -refreshToken"
  );
  return res
    .status(200)
    .json(new ApiResponse(200, SearchUser, "massage : done"));
});


export const addProductOnWiselist = asyncHandler(async (req, res) => {
  // add address

  const { area, city, state, pincode } = req.body;

  if (
    [area, city, state, pincode].some(
      (field) => field?.toString().trim() === ""
    )
  ) {
    throw new ApiError(400, "All fields are required");
  }

  try {
    const userAddress = await User.findById(req.userId).select("address");

    userAddress.address.push({ area, city, state, pincode });
    userAddress.save({ validateBeforeSave: false, new: true });
  } catch (error) {
    throw new ApiError(500, error || "Address not set");
  }

  const SearchUser = await User.findById(req.userId).select(
    "-password -refreshToken"
  );
  return res
    .status(200)
    .json(new ApiResponse(200, SearchUser, "massage : done"));
});


export const updateUserData = asyncHandler(async (req, res) => {
  // user Id
  // user new data -> email, fullName
  // Check if user is authenticated
  if (!req.userId) {
    throw new ApiError(400, "User not Authenticate");
  }
  // Check if request body is empty
  if (!req.body) {
    throw new ApiError(400, "No data received");
  }

  // Destructure email and fullName from request body
  const [email, fullName] = req.body;

  // Validate that email and fullName are provided and not empty
  if ([email, fullName].some((field) => field?.trim() === "")) {
    throw new ApiError(400, "These fields are required");
  }

  try {
    // Update user data by ID and return the updated document
    const updatedUser = await User.findByIdAndUpdate(
      req.userId,
      {
        $set: {
          email,
          fullName,
        },
      },
      { new: true }
    ).select("-password -refreshToken");
  } catch (error) {
    throw new ApiError(500, "User data not updated");
  }

  // Check if user data was not updated in the database
  if (!updatedUser) {
    throw new ApiError(500, "User data not updated in Database");
  }

  // Return success response with updated user data
  return res
    .status(200)
    .json(new ApiResponse(200, updatedUser, "User data updated successfully"));
});

export const updatePassword = asyncHandler(async (req, res) => {
  // user, userId (authentication not required)
  // match user details
  // old password
  // match password
  // set new password
  // return data

  // Check if request body is empty
  if (!req.body) {
    throw new ApiError(400, "No any Data received");
  }

  // Destructure userId, oldPassword, and newPassword from request body
  const [userId, oldPassword, newPassword] = req.body;

  // Validate that all fields are provided and not empty
  if (
    [userId, oldPassword, newPassword].some((field) => field?.trim() === "")
  ) {
    throw new ApiError(400, "All fields is required");
  }

  // Find user by ID and exclude refreshToken from the result
  const userData = await User.findById({ _id: userId }).select("-refreshToken");

  // Check if user data exists
  if (!userData) {
    throw new ApiError(409, "Invalid userId Or UserId Not Exits");
  }

  try {
    // Check if the old password is correct
    const checkOldPassword = await userData.isPasswordCorrect(oldPassword);
  } catch (error) {
    throw new ApiError(500, "Password checking failed");
  }
  if (!checkOldPassword) {
    throw new ApiError(409, "Incorrect Old password");
  }

  try {
    // Set new password and save user data
    userData.password = newPassword;
    userData.save({ validateBeforeSave: false });
  } catch (error) {
    throw new ApiError(500, error.message || "Failed to Update new password");
  }

  // Return success response
  return res.status(200).json(200, {}, "Password updated successfully");
});

export const changePassword = asyncHandler(async (req, res) => {
  // user login required
  // user id
  // body - newPassword
  // set password

  // Check if user is authenticated
  if (!req.userId) {
    throw new ApiError(400, "User not Authenticate");
  }

  // Check if request body is empty
  if (!req.body) {
    throw new ApiError(400, "No Data received");
  }

  // Find user by ID and exclude password and refreshToken from the result
  const userData = await User.findById(req.userId).select(
    "-password -refreshToken"
  );

  // Check if user data retrieval failed
  if (!userData) {
    throw new ApiError(500, "User Data retrieved failed");
  }

  try {
    // Set new password and save user data
    userData.password = newPassword;
    userData.save({ validateBeforeSave: false });
  } catch (error) {
    throw new ApiError(500, error.message || "User password not change");
  }

  // Return success response
  return res
    .status(200)
    .json(new ApiResponse(200, {}, "Password Change successfully"));
});

export const deleteUser = asyncHandler(async (req, res) => {
  // user id
  // delete
  // Check if user is authenticated
  if (!req.userId) {
    throw new ApiError(400, "User not Authenticate");
  }
  try {
    // Attempt to delete the user by ID
    const deletedUser = await User.findByIdAndDelete(req.userId);
  } catch (error) {
    // Handle any errors that occur during deletion
    throw new ApiError(500, error.message || "Failed to delete user");
  }

  // Check if the user was not deleted from the database
  if (!deletedUser) {
    throw new ApiError(500, "Failed to delete user from Database");
  }

  // Return success response indicating user was deleted
  return res
    .status(200)
    .json(new ApiResponse(200, {}, "User Successfully Deleted"));
});
