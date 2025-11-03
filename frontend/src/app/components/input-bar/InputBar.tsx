"use client";  // marker that allows for hooks to be handled in the browser rather than server

import { useState } from "react"; // stores memory 

export default function InputBar() {
  const [inputTerm, setInputTerm] = useState(""); // user input (question or command) to ChatGPT
  const [subreddit, setSubreddit] = useState(""); // subreddit input
  const [response, setResponse] = useState<string | null>(null); // data recieved from the backend
  const [loading, setLoading] = useState(false); // display progress of current task/post
  const [error, setError] = useState<string | null>(null); // gets error if it occurs

  // When user clicks submit, send POST request to FastAPI
  // Sets values of states by their defaults
  const handleSubmit = async () => {
    setLoading(true); 
    setError(null); 
    setResponse(null); 
    try {
      const res = await fetch("http://127.0.0.1:8000/input/", { //Send data from to backend endpoint
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ // converts Javascript objects to JSON strings
          input: inputTerm,
          subreddit: subreddit,
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch response"); // error if failed
      }

      const data = await res.json(); // waiting for a response from the backend from the POST
      setResponse(data.response); // sets response to data from backend
    } catch (err: unknown) { // otherwise shows error
      if (err instanceof Error) {
        setError(err.message); // error message from the backend
      } else {
        setError("An unknown error occurred."); // if we do not know the error
      }
    } finally {
      setLoading(false); // if data was recieved successfully, stop loading message//animation
    }

  };

  return (
    <div className="p-4 space-y-3 w-1/4 mx-auto text-white">
      <input // input bar
        type="text"
        value={inputTerm}
        onChange={(e) => setInputTerm(e.target.value)}
        placeholder="Ask a question..."
        className="border p-2 rounded w-full"
      />
      <label>Subreddit</label>
      <input // subreddit bar
        type="text"
        id="large-input"
        value={subreddit}
        onChange={(e) => setSubreddit(e.target.value)}
        placeholder="Enter a subreddit (e.g. AskReddit)"
        className="border p-2 rounded w-full"
      />
      <button // submit bar if loading: True show that its loading
        onClick={handleSubmit}
        disabled={loading}
        className="bg-white text-gray-700 px-4 py-2 rounded"
      >
        {loading ? "Loading..." : "Submit"}
      </button>
      {error && <p className="text-red-500">{error}</p>}
      {response && (
        <div className="relative left-1/2 -translate-x-1/2 mt-4 mb-4 p-3 border rounded bg-gray-50 w-[250%] mx-auto">
          <h3 className="font-bold mb-3 text-gray-700">
            AI Reddit-style Answer:
          </h3>
          <p className="text-gray-500">{response}</p>
        </div>
      )}
    </div> // if there is an error display it, display the response
  );
}
