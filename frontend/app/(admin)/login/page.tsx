import React from "react";

const page = () => {
  return (
    <div className="h-[85%] flex flex-col justify-center items-center ">
      <h2 className="text-lg md:text-xl font-extrabold mb-8 text-[#060709] ">
        LOGIN
      </h2>
      <form className="w-[80%] md:w-[40%] mx-auto">
        <div className="my-5">
          <label
            htmlFor="name"
            className=" block text-base font-medium text-[#060709]"
          >
            NAME/EMAIL: <span className="text-red-600">*</span>
          </label>
          <input
            type="text"
            name="text"
            id="name"
            placeholder="John Doe / johndoe@gmail.com"
            className="w-full border-b border-[#060709] pt-3  px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent "
          />
        </div>
        <div className="my-5">
          <label
            htmlFor="email"
            className="block text-base font-medium text-[#07074D]"
          >
            PASSWORD: <span className="text-red-600">*</span>
          </label>
          <input
            type="password"
            name="text"
            id="password"
            placeholder="**********"
            className="w-full border-b border-[#060709]  pt-3 px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent "
          />
        </div>
        <div className="flex flex-col items-center  md:flex-row md:justify-between">
          <div className="flex items-center mb-4">
            <input
              id="default-checkbox"
              type="checkbox"
              value=""
              className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded "
            />
            <label
              htmlFor="default-checkbox"
              className="ms-2  font-medium text-black"
            >
              REMEMBER
            </label>
          </div>
          <button className="text-[#D82126]">FORGOT PASSWORD</button>
        </div>

        <div className="flex justify-center my-12">
          <button className="hover:shadow-form  rounded-md bg-[#060709] py-3 px-8 text-center text-base font-semibold text-white outline-none">
            LOGIN
          </button>
        </div>
        <div className="flex justify-center my-12">
          <h2 className="text-sm md:text-md font-extrabold text-[#060709] ">
            HAVE AN ACCOUNT ?{" "}
            <a href="/sign-up" className="text-[#D82126] mr-1">
              SIGN UP
            </a>
            LOGIN INSTEAD.
          </h2>
        </div>
      </form>
    </div>
  );
};

export default page;
