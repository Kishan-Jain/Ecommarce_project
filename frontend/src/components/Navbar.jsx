import React from "react";

function Navbar() {
  return (
    <>
      <div className="h-12 w-full bg-orange-300 text-black text-2xl flex  items-center">
        <div>
          <a href="/">
            <strong className="text-red-600 font-sans text-opacity-80 px-2">
              Smart Baajar
            </strong>
          </a>
        </div>
        <div>
        <ul className="flex flex-row items-center bg-transparent">
            <li>
              <a
                href="#"
                className="block text-yellow-800 mx-2 text-lg font-serif md:hover:font-bold"
              >
                Home
              </a>
            </li>
            <li>
              <a
                href="#"
                className="block text-yellow-800 mx-2 text-lg font-serif md:hover:font-bold"
              >
                About
              </a>
            </li>
            <li>
              <a
                href="#"
                className="block text-yellow-800 mx-2 text-lg font-serif md:hover:font-bold"
              >
                Services
              </a>
            </li>
          </ul>
        </div>

        <div className="w-1/3 flex items-center justify-center mx-2 bg-orange-100 border-yellow-900 rounded-lg ">
          <div className="relative md:block flex-row">
            
            <input
              type="text"
              id="search-navbar"
              className="block py-1 ps-3 min-w-80 text-lg mx-2 text-gray-900 bg-orange-100 "
              placeholder="Search..."
            />
          </div>
            <button type="submit" id="search-navbar" className="block py-1 text-lg font-semibold font-serif">Search</button>
      
        </div>
        
      </div>
    </>
  );
}

export default Navbar;
