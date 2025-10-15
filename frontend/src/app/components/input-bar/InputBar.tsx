"use client";

import { useState } from "react";

export default function InputBar() {
  const [inputTerm, setInputTerm] = useState("");
  const [subreddit, setSubreddit] = useState("");
  const [response, setResponse] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // When user clicks submit, send POST request to FastAPI
  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/input/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          input: inputTerm,
          subreddit: subreddit,
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch response");
      }

      const data = await res.json();
      setResponse(data.response);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("An unknown error occurred.");
      }
    } finally {
      setLoading(false);
    }

  };

  return (
    <div className="p-4 space-y-3">
      <input
        type="text"
        value={inputTerm}
        onChange={(e) => setInputTerm(e.target.value)}
        placeholder="Ask a question..."
        className="border p-2 rounded w-full"
      />
      <input
        type="text"
        value={subreddit}
        onChange={(e) => setSubreddit(e.target.value)}
        placeholder="Enter a subreddit (e.g. AskReddit)"
        className="border p-2 rounded w-full"
      />
      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        {loading ? "Loading..." : "Submit"}
      </button>

      {error && <p className="text-red-500">{error}</p>}
      {response && (
        <div className="mt-4 p-3 border rounded bg-gray-50">
          <h3 className="font-bold mb-2">AI Reddit-style Answer:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}
