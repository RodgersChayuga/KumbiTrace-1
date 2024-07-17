import React from "react";
import Image from "next/image";

import { FaInstagram, FaTiktok } from "react-icons/fa";
import { FaXTwitter } from "react-icons/fa6";

const Footer = () => {
  return (
    <div className="mx-auto w-[90%] md:w-[60%] flex flex-col items-center ">
      <div className="flex md:flex-row flex-col justify-center items-center">
        <Image src="/fist-up.png" width={100} height={100} alt={""} />
        <div>
          <h3 className="text-lg md:text-xl font-bold text-[#D82126]">
            LET US GET OUR PEOPLE HOME
          </h3>
          <div className="flex justify-evenly mt-2">
            <FaXTwitter />
            <FaInstagram />
            <FaTiktok />
          </div>
        </div>
      </div>
      <h3 className="mb-8 mt-1"> &copy;2024 KumbiTrace. all rights reserved</h3>
    </div>
  );
};

export default Footer;
