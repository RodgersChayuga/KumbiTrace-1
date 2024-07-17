import React from "react";
import { IoSearchOutline, IoArrowForward } from "react-icons/io5";
import { FaLocationDot } from "react-icons/fa6";
import Gallery from "./ui/Gallery";

const PersonsGallery = () => {
  return (
    <div className="flex flex-col justify-center items-center mx-auto mt-5 md:pb-24 md:pt-12 w-[80%] md:w-full">
      <h2 className="text-2xl md:text-4xl font-extrabold text-[#D82126]">
        MISSING - ( 20 )
      </h2>
      <p className="my-4 text-xl text-gray-500 hidden md:inline-block">
        REPORT MISSING PERSON AS SOON AS POSSIBLE
      </p>
      <form method="GET" action="">
        <div className="border-b-2 border-gray-500 p-2 flex z-20">
          <span className="w-auto flex justify-end  items-center text-gray-500 px-2">
            <IoSearchOutline />
          </span>
          <input
            name="search"
            id="search"
            className="outline-none border-0 w-full bg-transparent px-2"
            type="text"
            placeholder="NAME/ID NUMBER/ CASE NUMBER"
          />
          <button
            type="submit"
            className=" hover:bg-gray-700 hover:text-white rounded-xl text-xl p-2 pl-4 pr-4 ml-2"
          >
            <IoArrowForward />
          </button>
        </div>
      </form>

      {/* <div className="flex p-4 gap-6 my-6 mx-auto">
        <input
          type="date"
          className="bg-transparent border-4 border-gray-500 rounded-lg px-2 "
        />
        <div className="border-4 border-gray-500 rounded-lg flex items-center pl-2">
          <FaLocationDot />
          <input
            type="text"
            placeholder="PLACE"
            className="bg-transparent ml-2 placeholder-black outline-none"
          />
        </div>
      </div> */}
      <h3 className="text-xl text-black font-extrabold pt-6">24/06/2024</h3>
      <h3 className="text-xl text-black font-extrabold">
        Nairobi, Mombasa, Kisumu
      </h3>
      <Gallery />
    </div>
  );
};

export default PersonsGallery;
