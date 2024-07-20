import React from "react";
import Organization from "./ui/Organization";

export const Hotline = () => {
  return (
    <div className="flex flex-col justify-center items-center mx-auto  mt-5 md:pb-24 md:pt-12">
      <h2 className="text-1xl md:text-3xl font-bold text-[#D82126]">
        CRITICAL HOTLINES
      </h2>
      <p className="my-4 text-xl text-gray-500 hidden md:inline-block">
        Should you, or anyone you know, find yourselves in a bind, these are
        some organizations you can reach out to.
      </p>

      <Organization />
    </div>
  );
};

export default Hotline;
