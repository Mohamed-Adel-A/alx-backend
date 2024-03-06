function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  const queueName = 'push_notification_code_3';

  jobs.forEach((jobFormat) => {
    const job = queue.create(queueName, jobFormat);

    job.save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errMessage) => {
      console.log(`Notification job ${job.id} failed: ${errMessage}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
