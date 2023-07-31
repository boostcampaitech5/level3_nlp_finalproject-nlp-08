import React, { useState, useEffect } from "react";

function Loader() {
  const phrases = [
    "데이터를 처리하고 있습니다...", 
    "답변을 생성중입니다... 잠시만 기다려주세요!", 
    "답변을 생성하는데 최대 30초 정도의 시간이 걸립니다... 잠시만 기다려주세요",
    "LawBot은 생성된 답변에 법적인 책임을 지지 않는 점 참고해주세요!",
    "상원이는 카사노바",
  ];

  const [currentPhraseIndex, setCurrentPhraseIndex] = useState(0);
  const [visibleText, setVisibleText] = useState("");

  const typingDelay = 100;
  const nextPhraseDelay = 3000; // 3초

  useEffect(() => {
    const typeText = (currentIndex, currentText) => {
      if (currentIndex < currentText.length) {
        setVisibleText(currentText.substring(0, currentIndex + 1));
        setTimeout(() => typeText(currentIndex + 1, currentText), typingDelay);
      } else {
        setTimeout(() => {
          setCurrentPhraseIndex((prevIndex) => (prevIndex + 1) % phrases.length);
          setVisibleText(""); 
        }, nextPhraseDelay);
      }
    };

    const currentPhrase = phrases[currentPhraseIndex];
    typeText(0, currentPhrase);
  }, [currentPhraseIndex]);

  return (
    <div className="animate-fade-up animate-delay-100 col-start-1 col-end-8 p-3 rounded-lg">
      <div className="flex flex-row items-center">
        <div className="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-300 flex-shrink-0">
          L
        </div>
        <div className="relative justify-center ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl">
          <div className="flex justify-center items-center">
            <img
              className="h-4 w-4"
              src="https://icons8.com/preloaders/preloaders/1488/Iphone-spinner-2.gif"
              alt=""
            />
            <div>{visibleText}</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Loader;
