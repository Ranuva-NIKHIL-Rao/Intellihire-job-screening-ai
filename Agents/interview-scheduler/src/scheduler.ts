export class Scheduler {
    private interviews: { id: number; date: Date; candidate: string; }[] = [];
    private nextId: number = 1;

    addInterview(date: Date, candidate: string): number {
        const interview = { id: this.nextId++, date, candidate };
        this.interviews.push(interview);
        return interview.id;
    }

    removeInterview(id: number): boolean {
        const index = this.interviews.findIndex(interview => interview.id === id);
        if (index !== -1) {
            this.interviews.splice(index, 1);
            return true;
        }
        return false;
    }

    listInterviews(): { id: number; date: Date; candidate: string; }[] {
        return this.interviews;
    }
}