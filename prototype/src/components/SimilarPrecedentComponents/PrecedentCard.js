function PrecedentCard({ precedent }) {
    return (
        <div class="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">유사 판례 조항 3</h5>
            <p class="font-small text-gray-700 dark:text-gray-400">사건 케이스 : {precedent.case_name}</p>
            <p class="font-small text-gray-700 dark:text-gray-400">사건 번호 : {precedent.case_number}</p>
            <p class="font-small text-gray-700 dark:text-gray-400">사건 분류 : {precedent.case_type}</p>
            <p class="font-small text-gray-700 dark:text-gray-400">관련 법 조항 :{precedent.ref_article}</p>
            <a href={precedent.url} class="mt-2 inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Read more
                <svg class="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9" />
                </svg>
            </a>
        </div>
    )
}
export default PrecedentCard
