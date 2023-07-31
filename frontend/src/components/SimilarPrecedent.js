import PrecedentCard from "./SimilarPrecedentComponents/PrecedentCard";

function SimilarPresdent({ precedents }) {
    const validPrecedents = precedents || [];
    
    return (
        <div className="w-full overflow-x-hidden">
            <aside
                id="separator-sidebar"
                className="fixed top-12 right-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
                aria-label="Sidebar"
            >
                <div className="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
                    <ul className="space-y-2 font-medium mt-2 mb-2">
                        {validPrecedents.map((validPrecedents, index) => (
                            <PrecedentCard key={index} precedent={validPrecedents} number={index + 1} />
                        ))}
                    </ul>
                </div>
            </aside>
        </div>
    );
}

export default SimilarPresdent;