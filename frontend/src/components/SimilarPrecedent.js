import PrecedentCard from "./SimilarPrecedentComponents/PrecedentCard"

function SimilarPresdent({ precedents }) {
    const precedents_best = precedents[0]
    const precedents_second = precedents[1]
    const precedents_third = precedents[2]

    return (
        <div className="w-full overflow-x-hidden">
            <aside id="separator-sidebar" className="fixed top-12 right-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
                <div className="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
                    <ul className="space-y-2 font-medium mt-2 mb-2">
                        <PrecedentCard precedent={precedents_best} number={1} />
                    </ul>
                    <ul className="space-y-2 font-medium mt-2 mb-2">
                        <PrecedentCard precedent={precedents_second} number={2} />
                    </ul>
                    <ul className="space-y-2 font-medium mt-2 mb-2">
                        <PrecedentCard precedent={precedents_third} number={3} />
                    </ul>
                </div>
            </aside>s
        </div>
    )
}
export default SimilarPresdent
