
import { ReactNode } from 'react'

interface ContentProps {
  children: ReactNode
}

export function Content({ children }: ContentProps) {
  return (
    <div className="flex-col flex">
      <div className="flex-1 space-y-4">
        {children}
      </div>
    </div>
  )
}
