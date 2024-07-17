"use client";

import Image from "next/image";
import React, { useState } from "react";
import { IoArrowForward, IoArrowBack } from "react-icons/io5";
import { data_org } from "../../data_org";

interface Company {
  id?: number;
  url: string;
  organizarion: string;
  website: string;
  email: string;
  phone: string;
}

const Organization = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 3;

  // Calculate total pages
  const totalPages = Math.ceil(data_org.length / itemsPerPage);

  const handlePageChange = (pageNumber: number) => {
    setCurrentPage(pageNumber);
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = Math.min(startIndex + itemsPerPage, data_org.length); // Ensures endIndex doesn't exceed data length

  const slicedData = data_org.slice(startIndex, endIndex); // Slice data based on pagination

  return (
    <>
      <div className="grid grid-cols-1 content-center md:grid-cols-3 md:w-[60%] mx-auto">
        {slicedData.map((org) => (
          <Company
            key={org.id}
            url={org.url}
            organizarion={org.organizarion}
            website={org.website}
            email={org.email}
            phone={org.phone}
          />
        ))}
      </div>
      <Pagination
        currentPage={currentPage}
        totalPages={totalPages}
        handlePageChange={handlePageChange}
      />
    </>
  );
};

const Company = ({ id, url, organizarion, website, email, phone }: Company) => {
  return (
    <div className=" flex flex-col items-center gap-2 m-2  border border-black rounded-xl  ">
      <Image
        src={url}
        alt={organizarion}
        height={400}
        width={400}
        className="object-contain  rounded-m"
      />
      <div className=" text-black text-xl md:text-2xl font-extrabold">{organizarion}</div>
      <div className=" text-black text-xl md:text-2xl font-extrabold">{phone}</div>
      <div className=" text-black text-xl md:text-2xl font-extrabold">{email}</div>
    </div>
  );
};

const Pagination = ({
  currentPage,
  totalPages,
  handlePageChange,
}: {
  currentPage: number;
  totalPages: number;
  handlePageChange: (pageNumber: number) => void;
}) => {
  const handlePrevClick = (currentPage: number) => {
    if (currentPage > 1) {
      handlePageChange(currentPage - 1);
    }
  };

  const handleNextClick = (currentPage: number) => {
    if (currentPage < totalPages) {
      handlePageChange(currentPage + 1);
    }
  };

  return (
    <div className="flex justify-center mt-4 items-center gap-4">
      <button
        className="flex items-center justify-center px-2 h-7 text-base font-medium text-gray-500  border-2 border-gray-800 rounded-lg hover:border-gray-600 hover:text-gray-700"
        disabled={currentPage === 1}
        onClick={() => handlePrevClick(currentPage)}
      >
        <IoArrowBack />
      </button>
      <button
        className="flex items-center justify-center px-2 h-7 text-base font-medium text-gray-500  border-2 border-gray-800 rounded-lg hover:border-gray-600 hover:text-gray-700 "
        disabled={currentPage === totalPages}
        onClick={() => handleNextClick(currentPage)}
      >
        <IoArrowForward className="font-bold" />
      </button>
    </div>
  );
};
export default Organization;
