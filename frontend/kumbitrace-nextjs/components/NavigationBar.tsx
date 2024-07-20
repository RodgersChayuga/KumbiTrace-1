"use client";

import React from "react";
import Image from "next/image";
import { useState } from "react";
import { FaBarsStaggered } from "react-icons/fa6";
import { MdChevronRight } from "react-icons/md";
import { AiOutlineClose } from "react-icons/ai";

import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
} from "@headlessui/react";

const NavigationBar = () => {
  const [toggleMenu, setToggleMenu] = useState(false);
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth={1.5}
    stroke="currentColor"
    className="size-6"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
    />
  </svg>;

  return (
    <nav className="sticky top-0 border-b-0 bg-[#F0E5D2]">
      <div className=" mx-auto w-[90%] md:w-[80%] ">
        <div className="flex mx-auto justify-between  ">
          {/* Primary menu and logo */}
          <div className="flex items-center gap-4 mt-2  justify-between w-full">
            {/* logo */}
            <a
              href="/"
              className="flex gap-1 font-bold text-black items-center "
            >
              <Image src="/fist-up.png" width={80} height={80} alt={""} />
              <span>ONE PEOPLE</span>
            </a>
            <div className="hidden lg:flex gap-16 justify-center items-center">
              <a
                href="/"
                className="  font-semibold flex items-center gap-2 hover:text-[#24292F]/80"
              >
                HOME {<MdChevronRight />}
              </a>
              {/* <a href="#">ABOUT</a> */}
              <a
                href="/login"
                className=" font-semibold flex items-center gap-2 hover:text-[#24292F]/80"
              >
                LOGIN{<MdChevronRight />}
              </a>
              <a
                href="/submit"
                className="text-white hover:text-black bg-[#24292F] hover:bg-[#ffffff] hover:border hover:border-[#24292F] rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center  me-2 mx-auto "
              >
                SUBMIT
              </a>
            </div>
            {/* primary */}
          </div>
          {/* secondary */}
          {/* Mobile navigation toggle */}
          <div className="lg:hidden flex items-center">
            <button onClick={() => setToggleMenu(!toggleMenu)}>
              {toggleMenu ? (
                <AiOutlineClose className="h-6" />
              ) : (
                <FaBarsStaggered className="h-6" />
              )}
            </button>
          </div>
        </div>
      </div>
      {/* mobile navigation */}

      <div
        className={`fixed  bg-[#F0E5D2] overflow-hidden flex flex-col lg:hidden gap-12  origin-top duration-700 ${
          !toggleMenu ? "h-0 w-full" : "h-full w-full z-40"
        }`}
      >
        <div className="border-t border-t-1 border-[#24292F]">
          <div className="pb-8 w-[70%] mx-auto z-40 mt-6">
            <div className="mx-auto divide-y divide-white/5 rounded-xl ">
              <div className="flex flex-col text-black ">
                <a
                  href="/"
                  className="pb-6 px-6 font-semibold flex items-center gap-4 hover:text-[#24292F]/80"
                >
                  HOME {<MdChevronRight />}
                </a>
                {/* <a href="#">ABOUT</a> */}
                <a
                  href="/login"
                  className="pb-6 px-6 font-semibold flex items-center gap-4 hover:text-[#24292F]/80"
                >
                  LOGIN{<MdChevronRight />}
                </a>
              </div>
            </div>

            <p className="mt-8">
              For submission of a person who is missing, please share the
              information here.
            </p>
            <a
              href="/submit"
              className="text-white hover:text-black bg-[#24292F] hover:bg-[#ffffff] hover:border hover:border-[#24292F] font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center  me-2 mb-2 mx-auto mt-12"
            >
              SUBMIT
            </a>
          </div>
        </div>
      </div>
      <hr className="h-px bg-gray-400 border-0 dark:bg-gray-700"></hr>
    </nav>
  );
};

export default NavigationBar;
