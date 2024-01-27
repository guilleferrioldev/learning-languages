import './App.css'
import { Card } from './card.jsx'

const users = [
  {
    userName: "guilleferrioldev",
    name: "Guille Ferriol",
    isFollowing: true
  },
  {
    userName: "midudev",
    name: "Miguel Ángel Durán",
    isFollowing: true
  },
  {
    userName: "pheralb",
    name: "Pablo Hernández",
    isFollowing: false
  },
  {
    userName: "elonmusk",
    name: "Elon Musk",
    isFollowing: false
  },
]

export function App () {
    return (
      <section className="App"> 
        {
          users.map(user => {
            const {userName, name, isFollowing} = user
            return (
              <Card key={userName} userName={userName} initialIsFollowing={isFollowing}>
                {name}
              </Card>
            )
          })
        }
      </ section> 
    )
}