import Header from './components/Header';
import ChattingSideBar from './components/ChattingSideBar';
import SimilarPrecedent from './components/SimilarPrecedent';
import { useState } from 'react';

function App() {

  const [message, setMessage] = useState("");
  const [sentMessage, setSentMessage] = useState("");
  const [aianswer, setAianswer] = useState("")
  const [precedents, setPrecedents] = useState([
    {
      "case_name": "",
      "case_number": "",
      "case_type": "",
      "ref_article": "",
      "url": "string"
    },
    {
      "case_name": "",
      "case_number": "",
      "case_type": "",
      "ref_article": "",
      "url": "string"
    },
    {
      "case_name": "",
      "case_number": "",
      "case_type": "",
      "ref_article": "",
      "url": ""
    }
  ])

  const messagehandler = async (e) => {
    e.preventDefault();
    setMessage("");
    setPrecedents([
      {
        "case_name": "",
        "case_number": "",
        "case_type": "",
        "ref_article": "",
        "url": "string"
      },
      {
        "case_name": "",
        "case_number": "",
        "case_type": "",
        "ref_article": "",
        "url": "string"
      },
      {
        "case_name": "",
        "case_number": "",
        "case_type": "",
        "ref_article": "",
        "url": ""
      }
    ])
    console.log(message)
    console.log(sentMessage)
    setAianswer("")
    setSentMessage(message);
    console.log(message)
    console.log(sentMessage)
    const response = await fetch('/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ q_sentence: sentMessage }),
    });
    const data = await response.json()
    setAianswer(data.answer_sentence)
    setPrecedents(data.similar_precedent)
  };

  return (
    <div class="w-full overflow-x-hidden">
      <Header />
      <div class="flex h-screen antialiased text-gray-800">
        <div class="flex flex-row w-full overflow-x-hidden">
          <div class="flex flex-col py-8 pl-4 w-64 bg-white flex-shrink-0">
            <ChattingSideBar />
          </div>
          <div class="flex flex-col flex-auto p-6">
            <div class="flex flex-col flex-auto flex-shrink-0 rounded-2xl bg-gray-100 p-4 mt-12">
              <div class="flex flex-col h-full overflow-x-auto mb-4">
                <div class="flex flex-col">
                  <div class="grid grid-cols-12 gap-y-2">
                    {sentMessage && (
                      <div class="col-start-6 col-end-13 p-3 rounded-lg">
                        <div class="flex items-center justify-start flex-row-reverse">
                          <div class="flex items-center justify-center h-10 w-10 rounded-full text-white bg-indigo-500 flex-shrink-0">
                            U
                          </div>
                          <div class="relative mr-3 text-sm bg-indigo-100 py-2 px-4 shadow rounded-xl">
                            <div>{sentMessage}</div>
                          </div>
                        </div>
                      </div>
                    )}
                    {aianswer && (
                      <div class="col-start-1 col-end-8 p-3 rounded-lg">
                        <div class="flex flex-row items-center">
                          <div
                            class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-300 flex-shrink-0"
                          >
                            L
                          </div>
                          <div
                            class="relative ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl"
                          >
                            <div>{aianswer}</div>
                          </div>
                        </div>
                      </div>)}
                  </div>
                </div>
              </div>
              <div
                class="flex flex-row items-center h-16 rounded-xl bg-white w-full px-4"
              >
                <div>
                  <button
                    class="flex items-center justify-center text-gray-400 hover:text-gray-600"
                  >
                    <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"
                      ></path>
                    </svg>
                  </button>
                </div>
                <div class="flex-grow ml-4">
                  <form type="submit" class="relative w-full">
                    <input
                      type="text"
                      class="flex w-full border rounded-xl focus:outline-none focus:border-indigo-300 pl-4 h-10"
                      placeholder='법률 문제를 입력해주세요.'
                      value={message}
                      onChange={(e) => setMessage(e.target.value)}
                    />
                    <button
                      type="submit"
                      onClick={messagehandler}
                      class="absolute flex items-center justify-center h-full w-12 right-0 top-0 text-gray-400 hover:text-gray-600"
                    >
                      <svg
                        class="w-6 h-6"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        ></path>
                      </svg>
                    </button>
                  </form>
                </div>
                <div class="ml-4">
                  <button
                    class="flex items-center justify-center bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white px-4 py-1 flex-shrink-0"
                  >
                    <span>Send</span>
                    <span class="ml-2">
                      <svg
                        class="w-4 h-4 transform rotate-45 -mt-px"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                        ></path>
                      </svg>
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="flex flex-col py-8 w-64 bg-white flex-shrink-0">
            <SimilarPrecedent precedents={precedents} />
          </div>

        </div>
      </div>

    </div >
  );
}

export default App;
