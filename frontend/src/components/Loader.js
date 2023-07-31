function Loader() {
    return (
        <div className="animate-fade-up animate-delay-100 col-start-1 col-end-8 p-3 rounded-lg">
            <div className="flex flex-row items-center">
                <div
                    className="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-300 flex-shrink-0"
                >
                    L
                </div>
                <div
                    className="relative justify-center ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl"
                >
                    <div className="flex justify-center items-center">
                        <img class="h-4 w-4 " src="https://icons8.com/preloaders/preloaders/1488/Iphone-spinner-2.gif" alt="" />
                            법률적인 가이드를 생성 중입니다... 잠시만 기다려주세요!
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Loader