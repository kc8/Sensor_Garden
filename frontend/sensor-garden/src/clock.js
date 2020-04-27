import React, {useEffect} from 'react'

function Clock() {
  const [date, setDate] = React.useState(new Date())

  useEffect(() => {
    const interval = setInterval(() => {
      setDate(new Date())
    }, 1000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div>
      <h2>{date.toLocaleTimeString()}.</h2>
    </div>
  )
}


export default Clock;