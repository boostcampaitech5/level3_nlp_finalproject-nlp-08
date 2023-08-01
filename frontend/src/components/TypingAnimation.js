import React, { useState, useEffect } from "react";

function TypingAnimation({ text }) {
  const [visibleText, setVisibleText] = useState("");
  const typingDelay = 20; // 타이핑 딜레이 시간(ms)

  useEffect(() => {
    const typeText = (currentIndex) => {
      if (currentIndex < text.length) {
        setVisibleText(text.substring(0, currentIndex + 1));
        setTimeout(() => typeText(currentIndex + 1), typingDelay);
      }
    };

    typeText(0);
  }, [text]);

  return <div>{visibleText}</div>;
}

export default TypingAnimation;