import mongoose from 'mongoose'


const categorySchema = new mongoose.Schema({
    title : {
        type:String,
        required : [true, "this is required field" ],
        unique : [true, "Field already Exits!!!" ],

    },
    pic : {
        type : String,
        required: [true, "this is required field" ]
    }
})

export const Category = mongoose.model("Category", categorySchema);