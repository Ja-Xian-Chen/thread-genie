import InputBar from "./components/input-bar/InputBar";
import Chat from "./features/chat/Chat";
export default function Home() {
  return (
    <div className=" fixed w-screen h-screen bg-[#FEB4FF] min-h-screen overflow-y-auto">
      <div className="font-bold text-white text-7xl text-center p-10 pt-30">
        Thread Genie
      </div>
      <div className="font-medium text-center text-white text-4xl">
        Hey there! How can I help you today?
      </div>
      <InputBar />
      {/* <Chat /> */}
    </div>
  );
}
