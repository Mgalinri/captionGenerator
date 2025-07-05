'use client'
import { useState,useEffect } from 'react';
import ImageIcon from '@mui/icons-material/Image';
import Form from 'next/form';

//To-Do: Check if the image is empty
export default function home() {
  const [caption,setCaption] = useState("Hi");
  const [image,setImage] = useState(null);
  
 
  const handleImageUpload = (event) =>{
        event.preventDefault();
        async function obtainCaption(){
            const formData = new FormData(event.target);
            setImage(event.target[0].files[0]);
            formData.append('image_path', image);
            console.log("Form Data:", formData);
            const response = await fetch('http://127.0.0.1:8000/caption',{
            method: 'POST',
            credentials: "include",
            body: formData,
            })
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return await response.json();
        }
        obtainCaption()
        .then(data => { 
            setCaption(data.caption);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    
      useEffect(() => {console.log(caption)},[caption]);

  }
  return (
   <div className="flex flex-col h-screen w-screen text-onBackground gap-4 bg-background justify-center items-center">
   <Form onSubmit={handleImageUpload} className="flex flex-col items-center justify-center gap-4">
    <div className="flex p-12 rounded-lg flex-col items-center justify-center border-onBackground border-4 border-dashed">
    <ImageIcon className="text-primary" style={{fontSize: 50}}/>
    <input 
    className="text-onBackground"
     type="file" 
      accept="image/png, image/jpeg"
      />

    </div>
        <button className="bg-primary text-onPrimary p-2 rounded-sm " type="submit" >Obtain Caption</button>
       </Form> 
      <p >{caption}</p>
   </div>

  
  );
}