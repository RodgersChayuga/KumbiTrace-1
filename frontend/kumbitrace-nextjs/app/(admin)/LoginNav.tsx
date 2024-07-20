import React from 'react'
import Image from "next/image";

const LoginNav = () => {
  return (
    <div className="flex justify-center mt-4 ">
      <div className="flex gap-1 font-bold text-gray-700 items-center ">
        <Image src="/fist-up.png" width={100} height={100} alt={""} />
        <span className="font-extrabold text-xl text-[#060709] ">
          ONE PEOPLE
        </span>
      </div>
    </div>
  );
}

export default LoginNav