import { useRef, useState, useEffect } from 'react' 
/* useRef: Permite crear una referencia mutable que persiste durante todo el ciclo de vida del componente. 
Es útil para guardar cualquier valor que puedas mutar como un identificador, un elemento del DOM, etc... 
y que cada vez que cambia no vuelva a renderizarse*/

export function useSearch () {
    const [search, updateSearch] = useState('')
    const [error, setError] = useState(null)
    const isFirstInput = useRef(true)
  
    useEffect(() => {
        if (isFirstInput.current) {
            isFirstInput.current = search === ''
            return
        }

        if (search.startsWith(" ")) {
            updateSearch('')
            isFirstInput.current = true
            setError('Movies cant start with blank spaces')
            return
        }
      
        if (search === '') {
            setError('Cant search for an empty movie')
            return
        }
  
        if (search.match(/^\d+$/)) {
            setError('Cant search for a movie with a number')
            return
        }
  
        if (search.length < 3) {
            setError('Search must be at least 3 characters')
            return
        }
  
        setError(null)
        } , [search])
  
    return { search, updateSearch , error }
  }