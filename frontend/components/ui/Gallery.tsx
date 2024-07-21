"use client";

import Image from "next/image";
import React, { useEffect, useRef, useState } from "react";
import { IoSearchOutline, IoArrowForward, IoArrowBack } from "react-icons/io5";
import { data } from "../../data";

interface Person {
  id?: number;
  first_name: string;
  last_name: string;
  profile_url: string;
  gender: string;
  date: string;
}

const Trace = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const debouncedSearchTerm = useRef(searchTerm);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 3;

  console.log("data2: ", data);

  const handleSearchChange = (e: any) => {
    e.preventDefault(); // Prevent form submission
    setSearchTerm(e.target.value.toLowerCase()); // Ensure case-insensitive search
    const timeoutId = setTimeout(() => {
      debouncedSearchTerm.current = e.target.value.toLowerCase();
    }, 500); // Adjust delay (in milliseconds) as needed

    return () => clearTimeout(timeoutId); // Cleanup function for timeout
  };

  const filteredData = data.filter((person) => {
    const searchTermLower = debouncedSearchTerm.current.toLowerCase();
    return person.first_name.toString().includes(searchTermLower); // Filter by ID
  });

  // Calculate total pages
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  const handlePageChange = (pageNumber: number) => {
    setCurrentPage(pageNumber);
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const displayedData = filteredData.slice(startIndex, endIndex);

  return (
    <>
      <div className="grid grid-cols-1 content-center md:grid-cols-3 gap-6">
        {displayedData.length > 0 // Check for filtered results
          ? displayedData.map((person) => (
              <Person
                key={person.id}
                first_name={person.first_name}
                last_name={person.last_name}
                profile_url={person.profile_url}
                gender={person.gender}
                date={person.date}
              />
            ))
          : data.map(
              (
                person // Render all data if no filter matches
              ) => (
                <Person
                  key={person.id}
                  first_name={person.first_name}
                  last_name={person.last_name}
                  profile_url={person.profile_url}
                  gender={person.gender}
                  date={person.date}
                />
              )
            )}
      </div>
      <Pagination
        currentPage={currentPage}
        totalPages={totalPages}
        totalPersons={filteredData.length}
        handlePageChange={handlePageChange}
      />
    </>
  );
};

const Person = ({
  id,
  first_name,
  last_name,
  profile_url,
  gender,
  date,
}: Person) => {
  return (
    <div>
      <div className="card flex flex-col items-center gap-2 my-4">
        <Image
          src={profile_url}
          alt={`${first_name} ${last_name}`}
          height="400"
          width="400"
          className="object-contain border border-black rounded-md"
        />
        <div className=" text-black text-xl md:text-2xl font-extrabold">
          <h3>{`${first_name} ${last_name}`}, {gender}</h3>
        </div>
      </div>
    </div>
  );
};

const Pagination = ({
  currentPage,
  totalPages,
  handlePageChange,
  totalPersons,
}: {
  currentPage: number;
  totalPages: number;
  totalPersons: number;
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
export default Trace;
