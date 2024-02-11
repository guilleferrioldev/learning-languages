import { Suspense } from 'react'
import { fetchData } from './utils/fetchData'

const apiData = fetchData("https://jsonplaceholder.typicode.com/users")

function App () {
    const data = apiData.read();
  
    return (
      <div className="App">
        <h1>Fetching Like a Pro</h1>
        <Suspense fallback={<div>Loading...</div>}>
          <ul className='card'>
            {data?.map(
              (user) => (<li key={user.id}>{user.name}</li>)
            )}
          </ul>
        </Suspense>
      </div>
    )
  }
  
export default App