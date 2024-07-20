import React from "react";

const page = () => {
  return (
    <div className="mx-auto w-[90%] md:w-[60%] flex flex-col items-center">
      <div className="mb-16 flex flex-col items-center gap-4">
        <h2 className="text-2xl md:text-4xl font-extrabold text-[#D82126]">
          LET’S GET THEM HOME
        </h2>
        <p className="my-4 text-xl text-#060709] ">
          In light of the unfortunate disappearance of our fellow Kenyans, we
          aim to get all the needed data in one place so that no one is
          forgotten. Please make sure that the data you share is correct and up
          to date. This will help in gathering timely leads and also reduce
          backlog.
        </p>
      </div>
      {/* <div> */}
      <h2 className="text-2xl md:text-2xl font-bold text-[#D82126] ">
        MISSING PERSON’S FORM
      </h2>
      <form className="w-[90%] mx-auto mt-8">
        <div className="-mx-3 flex flex-col gap-6 md:flex-row mb-10">
          <div className="w-full px-3 ">
            <label
              htmlFor="date"
              className="block text-base font-medium text-#060709]"
            >
              FULL NAME: <span className="text-red-600">*</span>
            </label>
            <input
              type="text"
              name="text"
              id="full-name"
              className="w-full border-b border-[#060709]   px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent placeholder-[#060709]"
            />
          </div>
          <div className="w-full px-3 ">
            <label
              htmlFor="time"
              className="block text-base font-medium text-#060709]"
            >
              AGE: <span className="text-red-600">*</span>
            </label>
            <input
              type="text"
              name="text"
              id="age"
              className="w-full border-b border-[#060709]  px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent placeholder-[#060709]"
            />
          </div>
        </div>
        <div className="my-5">
          <label
            htmlFor="phone"
            className=" block text-base font-medium text-[#07074D]"
          >
            MISSING DATE: <span className="text-red-600">*</span>
          </label>
          <input
            type="text"
            name="text"
            id="date"
            className="w-full border-b border-[#060709]   px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent placeholder-[#060709]"
          />
        </div>
        <div className="my-5">
          <label
            htmlFor="email"
            className="block text-base font-medium text-[#07074D]"
          >
            LAST KNOWN LOCATION: <span className="text-red-600">*</span>
          </label>
          <input
            type="text"
            name="text"
            id="location"
            className="w-full border-b border-[#060709]  py-3 px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent placeholder-[#060709]"
          />
        </div>

        <div className="my-5">
          <label
            htmlFor="email"
            className="block text-base font-medium text-#060709]"
          >
            AREA OF RESIDENCE: <span className="text-red-600">*</span>
          </label>
          <input
            type="text"
            name="text"
            id="residence_area"
            className="w-full border-b border-[#060709]  py-3 px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent placeholder-[#060709]"
          />
        </div>
        <div className="my-5">
          <label
            htmlFor="email"
            className="block text-base font-medium text-#060709]"
          >
            YOUR CONTACT LOCATION: <span className="text-red-600">*</span>
          </label>
          <input
            type="text"
            name="text"
            id="location"
            className="w-full border-b border-[#060709]  py-3 px-1 text-base font-medium text-[#6B7280] outline-none bg-transparent placeholder-[#060709]"
          />
        </div>

        <div className="w-full mb-4">
          <label
            htmlFor="email"
            className="block text-base font-medium text-#060709]"
          >
            PHOTO: <span className="text-red-600">*</span>
          </label>
          <div className="items-center justify-center mx-auto mb-2">
            <label
              className="flex justify-center w-full h-32 px-4 transition  border-2 border-[#060709] rounded-2xl appearance-none cursor-pointer hover:border-gray-400 focus:outline-none"
              id="drop"
            >
              <span className="flex items-center space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-6 h-6 text-gray-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                  ></path>
                </svg>
                <span className="font-medium text-gray-600">
                  Drop files to Attach, or
                  <span className="text-blue-600 underline ml-[4px]">
                    browse
                  </span>
                </span>
              </span>
              <input
                type="file"
                name="file_upload"
                className="hidden"
                accept="image/png,image/jpeg"
                id="input"
              />
            </label>
          </div>
          <p className="text-sm">BE SURE TO USE THE MOST RECENT AND CLEAREST IMAGE.</p>
        </div>
        <div>
          <label
            htmlFor="message"
            className="block text-base font-medium text-#060709]"
          >
            ANY OTHER INFORMATION:
          </label>
          <textarea
            id="message"
            className="block p-2.5 w-full text-sm text-gray-900 bg-transparent  rounded-lg border border-[#060709]"
            placeholder="Write your thoughts here..."
          ></textarea>
        </div>

        <div className="flex justify-center my-6">
          <button className="hover:shadow-form  rounded-md bg-[#060709] py-3 px-8 text-center text-base font-semibold text-white outline-none">
            Report
          </button>
        </div>
      </form>
      {/* </div> */}
    </div>
  );
};

export default page;
