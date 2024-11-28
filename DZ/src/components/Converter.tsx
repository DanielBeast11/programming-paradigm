import React, { useState } from "react";
import { transform } from "../utils/transform";

const Converter: React.FC = () => {
  const [input, setInput] = useState<string>("");
  const [result, setResult] = useState<string>("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInput(event.target.value);
  };

  const handleConvert = () => {
    try {
      const [katakana, syllables] = transform(input);
      setResult(`
        Katakana: ${katakana.join("")}
        Syllables: ${syllables.join("-")}
      `);
    } catch (error) {
      setResult("Error occurred during transformation");
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Конвертер</h1>
      <input
        type="text"
        value={input}
        onChange={handleChange}
        placeholder="Введите слово..."
        style={{
          padding: "10px",
          fontSize: "16px",
          width: "300px",
          marginBottom: "10px",
        }}
      />
      <br />
      <button
        onClick={handleConvert}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer",
          backgroundColor: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "5px",
        }}
      >
        Конвертировать
      </button>
      <div
        style={{
          marginTop: "20px",
          whiteSpace: "pre-wrap",
          fontSize: "14px",
          color: "#333",
        }}
      >
        {result}
      </div>
    </div>
  );
};

export default Converter;