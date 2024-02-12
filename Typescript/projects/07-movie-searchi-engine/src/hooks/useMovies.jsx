import { searchMovies } from '../services/movies'
import { useState, useRef, useMemo, useCallback} from 'react'

export function useMovies({ search, sort }) {
    const [movies, setMovies] = useState([])
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)
    const previousSearch = useRef(search)

    const getMovies = useCallback(async ({search}) => {
      if (search === previousSearch.current) return

      try {
        setLoading(true)
        setError(null)
        previousSearch.current = search
        const newMovies = await searchMovies({ search })
        setMovies(newMovies)
      } catch (e){
        setError(e.message)
      } finally {
        setLoading(false)
      }
    }, [])

    const sortedMovies = useMemo(() => {
      if (!movies) return;
      return sort
             ? [...movies].sort((a, b) => a.title.localeCompare(b.title))
             : movies
    }, [sort, movies])

    return { movies: sortedMovies, getMovies, loading}
}