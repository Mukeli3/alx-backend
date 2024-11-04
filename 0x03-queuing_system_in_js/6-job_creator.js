#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue({name: 'push notification code'});

const job = queue.create('push_notification_code', {
  phone: ''
  msg: 'Account registered',
});

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  })
job.save();
