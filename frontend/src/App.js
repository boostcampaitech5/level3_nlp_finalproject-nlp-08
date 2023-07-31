import Header from './components/Header';
import Loader from './components/Loader';
import ChattingSideBar from './components/ChattingSideBar';
import SimilarPrecedent from './components/SimilarPrecedent';
import { useState } from 'react';

function App() {
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState("");
  const [sentMessage, setSentMessage] = useState("");
  const [aianswer, setAianswer] = useState("");
  const [precedents, setPrecedents] = useState(null);

  const messagehandler = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("")
    setSentMessage(message)
    setAianswer("")
    setPrecedents(null)
    console.log(message)
    const response = await fetch('/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ q_sentence: message }),
    });
    const data = await response.json();
    
    console.log(message)
    console.log(data)
    if (data != null) {
      if (data.answer_sentence == null){
        setAianswer("죄송합니다만 저는 법률적인 내용에 관련하여 도움을 드리는 AI LawBot입니다. 법률적인 내용 외의 질문은 답변해드리지 않는 점 참고부탁드립니다. 법률적인 질문이 있으시다면 언제든지 물어보세요. 제가 최대한 자연스럽고 이해하기 쉽게 답변해 드리겠습니다. 어떤 도움이 필요하신가요?")
        setPrecedents(null)
      }
      else{
        setAianswer(data.answer_sentence);
        setPrecedents(data.similar_precedent);
      }
    }
    setLoading(false)
  };

  return (
    <div className="w-full overflow-x-hidden">
      <Header />
      <div className="flex h-screen antialiased text-gray-800">
        <div className="flex flex-row w-full overflow-x-hidden">
          <div className="flex flex-col py-8 pl-4 w-64 bg-white flex-shrink-0">
            <ChattingSideBar />
          </div>
          <div className="flex flex-col flex-auto p-6">
            <div className="flex flex-col flex-auto flex-shrink-0 rounded-2xl bg-gray-100 p-4 mt-12">
              <div className="flex flex-col h-full overflow-x-auto mb-4">
                <div className="flex flex-col">
                  <div className="grid grid-cols-12 gap-y-2">
                    {sentMessage && (
                      <div className="animate-fade-up animate-delay-100 col-start-6 col-end-13 p-3 rounded-lg">
                        <div className="flex items-center justify-start flex-row-reverse">
                          <div className="flex items-center justify-center h-10 w-10 rounded-full text-white bg-indigo-500 flex-shrink-0">
                            U
                          </div>
                          <div className="animate-fade-up relative mr-3 text-sm bg-indigo-100 py-2 px-4 shadow rounded-xl">
                            <div>{sentMessage}</div>
                          </div>
                        </div>
                      </div>
                    )}
                    {aianswer && (
                      <div className="animate-fade-up animate-delay-100 col-start-1 col-end-8 p-3 rounded-lg">
                        <div className="flex flex-row items-center">
                          <div
                            className="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-300 flex-shrink-0"
                          >
                            L
                          </div>
                          <div
                            className="relative ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl"
                          >
                            <div>{aianswer}</div>
                          </div>
                        </div>
                      </div>)}
                      {!aianswer && loading && (<Loader />)}
                  </div>
                </div>
              </div>
              <form
                className="flex flex-row items-center h-16 rounded-xl bg-white w-full px-4"
                onSubmit={messagehandler}
              >
                <div>
                  <button
                    className="flex items-center justify-center text-gray-400 hover:text-gray-600"
                  >
                    <svg
                      className="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"
                      ></path>
                    </svg>
                  </button>
                </div>

                <div className="flex-grow ml-4">
                  <div className="relative w-full">
                    <input
                      type="text"
                      className="flex w-full border rounded-xl focus:outline-none focus:border-indigo-300 pl-4 h-10"
                      placeholder='법률 문제를 입력해주세요.'
                      value={message}
                      onChange={(e) => setMessage(e.target.value)}
                    />
                    <button
                      className="absolute flex items-center justify-center h-full w-12 right-0 top-0 text-gray-400 hover:text-gray-600"
                    >
                      <svg
                        className="w-6 h-6"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        ></path>
                      </svg>
                    </button>
                  </div>
                </div>
                <div className="ml-4">
                  <button
                    type="submit"
                    className="flex items-center justify-center bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white px-4 py-1 flex-shrink-0"
                  >
                    <span>Send</span>
                    <span className="ml-2">
                      <svg
                        className="w-4 h-4 transform rotate-45 -mt-px"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                        ></path>
                      </svg>
                    </span>
                  </button>
                </div>

              </form>
            </div>
          </div>
          <div className="flex flex-col py-8 w-64 bg-white flex-shrink-0">
            <SimilarPrecedent precedents={precedents} />
          </div>

        </div>
      </div>

    </div >
  );
}

export default App;
