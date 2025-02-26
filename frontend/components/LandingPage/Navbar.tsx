import { UserButton } from "@clerk/nextjs";
import { currentUser } from "@clerk/nextjs/server";
import Link from "next/link";

async function Navbar() {
  const user = await currentUser();

  return (
    <nav className="flex justify-between items-center p-4">
      <Link href="/" className="bg-blue-500 text-white px-4 py-2 rounded-md">
        Salary Benchmark Ai
      </Link>
      <div className="flex items-center gap-4">
        {user ? (
          <UserButton />
        ) : (
          <>
            <Link
              href="/sign-in"
              className="bg-blue-500 text-white px-4 py-2 rounded-md"
            >
              Sign In
            </Link>
            <Link
              href="/sign-up"
              className="bg-blue-500 text-white px-4 py-2 rounded-md"
            >
              Sign Up
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
