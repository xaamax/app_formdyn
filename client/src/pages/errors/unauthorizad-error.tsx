import { Button } from '@/components/ui/button'

function UnauthorizadError() {
  return (
    <div className='h-svh'>
      <div className='m-auto flex h-full w-full flex-col items-center justify-center gap-2'>
        <h1 className='text-[7rem] leading-tight font-bold'>401</h1>
        <span className='font-medium'>
          Oops! Você não tem permissão para acessar esta página.
        </span>
        <p className='text-muted-foreground text-center'>
          Parece que você tentou acessar um recurso que requer autenticação
          adequada. <br />
          Por favor, faça login com as suas credenciais .
        </p>
        <div className='mt-6 flex gap-4'>
          <Button onClick={() => window.location.href = '/login'}>Autenticar</Button>
        </div>
      </div>
    </div>
  )
}

export default UnauthorizadError
