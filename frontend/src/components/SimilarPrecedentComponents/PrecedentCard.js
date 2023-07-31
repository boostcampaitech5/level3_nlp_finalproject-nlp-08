function PrecedentCard({ precedent, number }) {
    return (
        <div className="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">유사 판례 조항 {number}</h5>
            <p className="font-small text-gray-700 dark:text-gray-400">사건 이름 : {precedent.case_name}</p>
            <p className="font-small text-gray-700 dark:text-gray-400">사건 번호 : {precedent.case_number}</p>
            <p className="font-small text-gray-700 dark:text-gray-400">사건 분류 : {precedent.case_type}</p>
            <p className="font-small text-gray-700 dark:text-gray-400">관련 법 조항 :{precedent.ref_article}</p>
            <a href={precedent.url} target="_blank" rel="noopener noreferer nofollow" className="mt-2 inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Read more
                <svg className="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 5h12m0 0L9 1m4 4L9 9" />
                </svg>
            </a>
        </div>
    )
}
export default PrecedentCard
