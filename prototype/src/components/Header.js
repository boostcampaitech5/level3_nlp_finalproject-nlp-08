import lawbot from "../asset/lawbot.png"

function Header() {
    return (
        <nav class="fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
            <div class="px-3 py-3 lg:px-5 lg:pl-3">
                <div class="flex items-center justify-between">
                    <div class="flex items-center justify-start">
                        <img src={lawbot} class="h-8 mr-3" alt="FlowBite Logo" />
                        <span class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white">
                            LawBot
                        </span>
                    </div>
                </div>
            </div>
        </nav>
    )
}
export default Header
