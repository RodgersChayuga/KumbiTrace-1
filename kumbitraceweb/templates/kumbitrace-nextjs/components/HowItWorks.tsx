import React from "react";
import { LuFileInput } from "react-icons/lu";
import { FaLongArrowAltRight } from "react-icons/fa";
import { RiVerifiedBadgeLine } from "react-icons/ri";
import { AiOutlinePushpin } from "react-icons/ai";

const HowItWorks = () => {
  return (
    <div className="flex flex-col items-center justify-center gap-12 md:py-24">
      <h2 className="text-1xl md:text-3xl font-bold text-[#D82126]">
        HOW IT WORKS
      </h2>
      <div className="flex flex-col md:flex-row items-center justify-center gap-4">
        <div className="flex flex-col justify-center items-center gap-4">
          <LuFileInput className="text-8xl" />
          <h2 className="text-lg md:text-xl font-bold text-[#D82126]">
            SUBMIT
          </h2>
          <p>Information about Persons concerned.</p>
        </div>
        <div>
          <FaLongArrowAltRight className="text-4xl hidden md:inline-block" />
        </div>
        <div className="flex flex-col justify-center items-center gap-4">
          <RiVerifiedBadgeLine className="text-8xl" />
          <h2 className="text-lg md:text-xl font-bold text-[#D82126]">
            VERIFICATION
          </h2>
          <p>Information about Persons concerned.</p>
        </div>
        <div>
          <FaLongArrowAltRight className="text-4xl hidden md:inline-block" />
        </div>
        <div className="flex flex-col justify-center items-center gap-4">
          <AiOutlinePushpin className="text-8xl" />
          <h2 className="text-lg md:text-xl font-bold text-[#D82126]">
            POST
          </h2>
          <p>Information about Persons concerned.</p>
        </div>
      </div>
    </div>
  );
};

export default HowItWorks;
