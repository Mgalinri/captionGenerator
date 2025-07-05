import Image from "next/image";
import Link from 'next/link'

/*Landing page*/
/*Restructure this later*/
export default function Home() {
  return (
   <div className="bg-background  h-100vh w-screen flex flex-col  gap-4 items-center justify-center">
 
   <nav className="pt-10  flex flex-row justify-end pr-20 gap-4 w-full h-1/2 items-center">
    <Link  href="/signIn" className="text-onBackground font-bold">Log In</Link>
    <Link href="/signUp" className="text-onBackground font-bold">Sign Up</Link>
    </nav>

  
     <section className="flex flex-col items-center justify-center gap-4 p-10 w-full h-1/2 ">
      
     <h1 className="text-onBackground font-bold text-4xl text-wrap pr-10 pl-10"> I am <span className="bg-primary text-onPrimary">caption </span> generator, let me help you so you can focus on what matters the most.</h1>
    
 <div className=" relative aspect-square w-2/3 h-2/3 ">
     <Image  
     src='/img/landingPage_1.jpg' 
     alt="A women being carried by a men"  
     fill
     size="100vw"
     className="object-cover">

     </Image>
</div>
</section>
       
  
   </div>
  );
}
/*Just sign in and sign up missing*/
/*
<div className="h-screen w-screen flex flex-col items-center justify-center">
       <div className="flex flex-col items-center justify-center  text-black  p-20 rounded-lg border-dashed border-4 ">
        <label></label>
        <input type="file">
        </input>
       
        
    </div>
    <--- Add action to this button --->
     <button className="bg-black text-white mt-2 p-2 rounded-sm">Generate Caption</button>
    </div>*/

    /* <--- Picture Grid --->
    <div className="h-screen w-screen">
      <div className="grid grid-cols-3 grid-rows-3 gap-4">
        <div>Hwllo</div>
        <div>Hwllo</div>
        

      </div>
    </div>*/