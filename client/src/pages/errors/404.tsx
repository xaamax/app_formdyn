import { useNavigate } from 'react-router-dom'
import { Button } from '@/components/ui/button'

export function Error404() {
  const navigate = useNavigate();

  return (
    <div className='h-svh'>
      <div className='m-auto flex h-full w-full flex-col items-center justify-center gap-2'>
        <h1 className='text-[7rem] leading-tight font-bold'>404</h1>
        <span className='font-medium'>Oops! Página não encontrada!</span>
        <p className='text-muted-foreground text-center'>
          Parece que a página que você está procurando <br />
          não existe ou pode ter sido removida.
        </p>
        <div className='mt-6 flex gap-4'>
          <Button variant='outline' onClick={() => navigate(-1)}>
            Voltar a página anterior
          </Button>
        </div>
      </div>
    </div>
  )
}
