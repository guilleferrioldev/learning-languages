import { useState, useMemo} from 'react'
import "./App.css"
import { type User, SortBy } from './types.d'
import { ListOfUsers } from './components/ListOfUsers'
import { useInfiniteQuery} from '@tanstack/react-query'

const LIMIT = 10;

async function fetchUsers ({pageParam }: {pageParam: number}): Promise<{
  users: User[];
  currentPage: number;
  nextPage: number | null
}> {
  return await  fetch(`https://randomuser.me/api/?results=10&seed=guilleferrioldev&page=${pageParam}`)
  .then(async res => {
    if (!res.ok) throw new Error("Error fetching")
    return await res.json()})
  .then(res => {
    const currentPage = Number(res.info.page)
    return {
      users: res.results,
      currentPage: currentPage,
      nextPage: currentPage + 1 < LIMIT ? currentPage + 1 : null,
    }
  })
}

function App() {
  const { data, status, error, refetch, fetchNextPage, hasNextPage} = useInfiniteQuery({
    queryKey: ['users'],
    queryFn: fetchUsers,
    initialPageParam: 0,
    getNextPageParam: (lastPage) => lastPage.nextPage,
  })

  const users: User[] = data?.pages?.flatMap(page => page.users) ?? []
  
  const [showColors, setShowColors] = useState(false)
  const [sorting, setSorting] = useState<SortBy>(SortBy.NONE)
  const [filterCountry, setFilterCountry] = useState<string | null>(null)

  const toggleColors = () => {
    setShowColors(!showColors)
  }

  const toggleSortByCountry = () =>  {
    const newSortingValue = sorting == SortBy.NONE ? SortBy.COUNTRY : SortBy.NONE
    setSorting(newSortingValue)
  }

  const handleDelete = (email: string) => {
   // const filteredUsers = users.filter((user) => user.email !== email)
   // setUsers(filteredUsers)
  }

  const handleReset = () => {
    refetch()
  }

  const handleChangeSort = (sort: SortBy) => {
    setSorting(sort)
  }

  const filteredUsers =  useMemo(() => {
    return  filterCountry != null && filterCountry.length > 0
      ? users?.filter(user => {
      return user.location.country.toLowerCase().includes(filterCountry.toLocaleLowerCase())
  })
  : users
}, [users, filterCountry]) 

const sortedUsers = useMemo(() => {
  if (sorting === SortBy.NONE) return filteredUsers

  const compareProperties: Record<string, (user: User) => any> = {
    [SortBy.COUNTRY]: user => user.location.country,
    [SortBy.NAME]: user => user.name.first,
    [SortBy.LAST]: user => user.name.last
  }

  return filteredUsers?.toSorted((a, b) => {
    const extractProperty = compareProperties[sorting]
    return extractProperty(a).localeCompare(extractProperty(b))
  })
}, [filteredUsers, sorting])

  return (
    <div className="">
      <h1>Table scrolling</h1>
      <header>
          <button onClick={toggleColors}>
            Coloring files
          </button>
          <button onClick={toggleSortByCountry}>
            {sorting === SortBy.COUNTRY ? 'Dont sort by country' : 'Sort by Country'}
          </button>
          <button onClick={handleReset}>
            Reset
          </button>
          <input placeholder='Filter by country' onChange={(e) => 
            setFilterCountry(e.target.value)} />
      </header>
      <main>
        {users.length > 0 &&
        <ListOfUsers changeSorting={handleChangeSort}
                     deleteUser={handleDelete} 
                     showColors={showColors}
                     users={sortedUsers} />}
        {status === 'pending' && <strong>Loading</strong>}
        {status === 'error' && error && <p>An error was ocurred</p>}
        {status === 'success' && !error && users.length === 0 && <p>There are no users</p>}
        {status === 'success' && !error && hasNextPage === true && users.length > 0 &&
        <button onClick={() => fetchNextPage()}>
          More results
        </button> }
        {status === 'success' && !error && hasNextPage === false && users.length > 0 && <p>There is no more results</p>}
      </main>
      
    </div>
  )
}

export default App