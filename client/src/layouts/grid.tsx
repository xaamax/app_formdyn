
interface Props {
    cols?: string
    children?: React.ReactNode
}

export default (props: Props) => {

    const gridClass = () => {
        const cols = props.cols?.split(' ') ?? []
        const normalized = Array.from({ length: 4 }, (_, i) => cols[i] || '1')

        const [xs, sm, md, lg] = normalized

        return [
            'grid',
            `grid-cols-${xs}`,
            `sm:grid-cols-${sm}`,
            `md:grid-cols-${md}`,
            `lg:grid-cols-${lg}`,
        ].join(' ')
    }

    return (
        <div className={`${gridClass()} gap-4`}>
            {props.children}
        </div>
    )
}