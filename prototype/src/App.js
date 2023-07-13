import Header from './components/Header';
import ChattingSideBar from './components/ChattingSideBar';
import SimilarPrecedent from './components/SimilarPrecedent';

function App() {
  return (
    <div class="w-full overflow-x-hidden">
      <Header />
      <div class="flex h-screen antialiased text-gray-800">
        <div class="flex flex-row w-full overflow-x-hidden">
          <div class="flex flex-col py-8 pl-4 w-64 bg-white flex-shrink-0">
            <ChattingSideBar />
          </div>
          <div class="flex flex-col flex-auto p-6">
            <div
              class="flex flex-col flex-auto flex-shrink-0 rounded-2xl bg-gray-100 p-4 mt-12"
            >
              <div class="flex flex-col h-full overflow-x-auto mb-4">
                <div class="flex flex-col">
                  <div class="grid grid-cols-12 gap-y-2">
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
                          <div>안녕하세요? 법률 상담 LawBot입니다 무엇을 도와드릴까요?</div>
                        </div>
                      </div>
                    </div>

                    <div class="col-start-6 col-end-13 p-3 rounded-lg">
                      <div class="flex items-center justify-start flex-row-reverse">
                        <div
                          class="flex items-center justify-center h-10 w-10 rounded-full text-white bg-indigo-500 flex-shrink-0"
                        >
                          U
                        </div>
                        <div
                          class="relative mr-3 text-sm bg-indigo-100 py-2 px-4 shadow rounded-xl"
                        >
                          <div>저는 결혼한 지 10년 되었으나 남편의 부정행위로 인하여 이혼하기로 하고, 남편 명의의 주택을 팔아 위자료로 받았습니다. 그렇지만 그 동안 제가 가정에 기여한 것에 비해 부족하다고 생각되어 남편의 퇴직금에 대하여도 재산분할청구를 해보려고 합니다. 남편은 대기업체의 간부로 있어 만일 퇴직할 경우에는 퇴직금이 상당하거든요. 이것이 가능한지요?</div>
                        </div>
                      </div>
                    </div>

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
                          <div>네, 가능합니다. 대법원 판례에 따르면, 부부의 재산분할에 있어 퇴직금은 재산분할의 대상이 될 수 있습니다. 따라서 귀하는 남편의 퇴직금에 대한 재산분할청구를 할 수 있습니다. 다만, 재산분할의 비율은 혼인기간, 재산의 형성 및 유지에 기여한 정도, 부양의 필요성, 자녀의 양육비 등 여러 가지 사정을 고려하여 결정됩니다. 따라서 귀하의 경우, 혼인기간, 남편의 재산 형성에 대한 귀하의 기여도, 자녀의 양육비 등 여러 가지 사정을 고려하여 재산분할의 비율을 주장해야 합니다. 귀하의 경우, 남편의 부정행위로 인하여 이혼하게 되었고, 남편은 대기업의 간부로 있어 퇴직금이 상당하다는 점을 고려하여 재산분할의 비율을 높게 주장할 수 있을 것으로 보입니다. 그러나, 재산분할의 비율은 법원이 결정하는 것이므로, 귀하의 주장이 받아들여질지는 확실하지 않습니다. 따라서 귀하는 재산분할청구를 하기 전에 변호사와 상담하여 재산분할의 비율을 주장하는 것이 좋습니다.</div>
                        </div>
                      </div>
                    </div>

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
                  <div class="relative w-full">
                    <input
                      type="text"
                      class="flex w-full border rounded-xl focus:outline-none focus:border-indigo-300 pl-4 h-10"
                      placeholder='법률 문제를 입력해주세요.'
                    />
                    <button
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
                  </div>
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
            <SimilarPrecedent />
          </div>
        </div>
      </div>

    </div >
  );
}

export default App;
