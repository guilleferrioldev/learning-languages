import { useId } from "react"
import "./Filters.css"
import { useFilters } from "../hooks/useFilters"

export function Filters () {
    const { filters, setFilters } = useFilters()
    const minPriceFilterId = useId()
    const categoryFilterId = useId()

    const handleChangeMinPrice = (event) => {
        setFilters(prevState => ({
            ...prevState,
            minPrice: event.target.value,
        }))
    } 

    const handleChangeCategory = (event) => {
        setFilters(prevState => ({
            ...prevState,
            category: event.target.value,
        }))
    }

    return (
    <section className="filters">
        <div> 
            <label htmlFor={minPriceFilterId}>Min Price</label>
            <input 
                type="range"
                id={minPriceFilterId}
                min="0"
                max="1000"
                onChange={handleChangeMinPrice}
                value={filters.minPrice}
            />
            <span>{filters.minPrice}</span>
        </div>

        <div>
            <label htmlFor={categoryFilterId}>Category</label>
            <select id={categoryFilterId} onChange={handleChangeCategory}>
                <option value="all">All</option>
                <option value="laptops">Laptops</option>
                <option value="smartphones">Smartphones</option>
            </select>
        </div>
    </section>
    )
} 