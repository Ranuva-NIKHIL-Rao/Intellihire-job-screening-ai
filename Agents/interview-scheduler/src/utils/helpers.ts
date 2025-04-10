export function formatDate(date: Date): string {
    const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: true };
    return date.toLocaleDateString(undefined, options);
}

export function validateInput(input: string): boolean {
    return input.trim().length > 0;
}