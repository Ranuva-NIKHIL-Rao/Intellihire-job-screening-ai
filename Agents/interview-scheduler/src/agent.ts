class InterviewAgent {
    constructor(private scheduler: Scheduler) {}

    scheduleInterview(date: string, candidate: string): string {
        if (!validateInput(date, candidate)) {
            return 'Invalid input. Please provide a valid date and candidate name.';
        }
        return this.scheduler.addInterview(date, candidate);
    }

    cancelInterview(interviewId: string): string {
        return this.scheduler.removeInterview(interviewId);
    }

    rescheduleInterview(interviewId: string, newDate: string): string {
        if (!validateInput(newDate)) {
            return 'Invalid date. Please provide a valid date.';
        }
        return this.scheduler.rescheduleInterview(interviewId, newDate);
    }
}

export default InterviewAgent;