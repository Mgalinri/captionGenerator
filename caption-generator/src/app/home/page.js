import Image from "next/image";
import TextField from "@mui/material/TextField";
import ImageIcon from '@mui/icons-material/Image';


//To-Do: Add functionality to upload images
//To-Do: Add menu bar
export default function home() {
  return (
   <div className="flex flex-col h-screen w-screen text-onBackground gap-4 bg-background justify-center items-center">
    <div className="flex p-12 rounded-lg flex-col items-center justify-center border-onBackground border-4 border-dashed">
    <ImageIcon className="text-primary" style={{fontSize: 50}}/>
    <input className="text-onBackground" type="file"  accept="image/png, image/jpeg"></input>

    </div>
        <button className="bg-primary text-onPrimary p-2 rounded-sm " type="submit">Obtain Caption</button>
   </div>
  
  );
}