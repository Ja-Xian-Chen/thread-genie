import InputBar from "./components/input-bar/InputBar";
import Chat from "./features/chat/Chat";
export default function Home() {
  return (
    <div>
      <div>Thread Genie</div>
      <div>Hey there! How can I help you today?</div>
      <InputBar/>
      <Chat/>
    </div>
  );
}
