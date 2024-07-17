import NavigationBar from "@/components/NavigationBar";
import PersonsGallery from "@/components/PersonsGallery";
import HowItWorks from "@/components/HowItWorks";
import Hotline from "@/components/Hotline";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main className="">
      <PersonsGallery />
      <hr className="h-px my-8 bg-gray-400 border-0 dark:bg-gray-700"></hr>
      <HowItWorks />
      <hr className="h-px my-8 bg-gray-400 border-0 dark:bg-gray-700"></hr>
      <Hotline />
      <hr className="h-px my-8 bg-gray-400 border-0 dark:bg-gray-700"></hr>
    </main>
  );
}
