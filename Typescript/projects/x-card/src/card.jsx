import { useState } from 'react'

export function Card ({children, userName, initialIsFollowing}) {
    const [isFollowing, setIsFollowing] = useState(initialIsFollowing)

    const text = isFollowing ? 'Following' : 'Follow'
    const buttonClassName = isFollowing 
        ? 'x-card-button is-following'
        : 'x-card-button'

    const handleClick = () => {
        setIsFollowing(!isFollowing)
    }

    return (
      <article className="x-card">
        <header className="x-card-header">
          <img className="x-card-avatar" alt="avatar"
                src={`https://unavatar.io/${userName}`} />
          <div className="x-card-info">
            <strong>{children}</strong>
            <span className="x-card-info-username">@{userName}</span>
          </div>
        </header>
        
        <aside>
          <button className={buttonClassName} onClick={handleClick}>
            <span className="x-card-button-text">{text}</span>
            <span className="x-card-button-stopFollow">Unfollow</span>
          </button>
        </aside>
      </article>
    )
}