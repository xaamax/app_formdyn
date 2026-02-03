export interface PaginationResponseDTO<T> {
    items: T[]
    page_number: number
    page_size: number
    total_items: number
}