import Image from "next/image";
import TextField from "@mui/material/TextField";
import Link from 'next/link';
import "../globals.css";
import { red } from "@mui/material/colors";

export default function signIn() {
  return (
    <form className="h-screen w-screen text-onBackground flex flex-col items-center justify-center gap-4 bg-background">
    <TextField className="text-primary"  id="filled-basic" label="Username" variant="filled" />
    <TextField className="text-primary" id="filled-basic" label="Password" variant="filled" />
    <Link href="/home" className="bg-primary text-onPrimary p-2 rounded-lg" type="submit">Sign In</Link>
    </form>
  
  );
}